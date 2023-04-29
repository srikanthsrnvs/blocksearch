import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import Typed from 'typed.js';
import Skeleton from 'react-loading-skeleton'
import 'react-loading-skeleton/dist/skeleton.css'
import '../styles/SearchPage.css'

type ApiResponse = {
    data: any[];
    completion: string;
    sql: string;
};


const SearchPage: React.FC = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState<any[]>([]);
    const [completion, setCompletion] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);
    const typedRef = useRef<Typed | null>(null);
    const [sql, setSql] = useState<string | null>(null);

    useEffect(() => {
        // Initialize typed.js
        const options = {
            strings: [
                'What are the last 20 erc20 transfers?',
                'What is the balance of address 0x1234?',
                'How many transactions were made in the last hour?'
            ],
            typeSpeed: 20,
            backSpeed: 40,
            showCursor: false,
            loop: true
        };
        typedRef.current = new Typed('.search-bar-placeholder', options);

        // Clean up typed.js instance on unmount
        return () => {
            typedRef.current?.destroy();
        };
    }, []);

    const handleSearch = async () => {
        setLoading(true);
        try {
            const response = await axios.get<ApiResponse>(`http://127.0.0.1:5000/search/eth?query=${query}`);
            if (response.data.data.length === 0) {
                alert('No results found');
            }
            setResults(response.data.data);
            setCompletion(response.data.completion);
            setSql(response.data.sql); // Set the SQL state
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };


    const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

    const downloadJsonData = () => {
        const data = JSON.stringify(results, null, 2);
        const blob = new Blob([data], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'data.json';
        link.click();
    };
    
    const shouldShowDownloadButton = results.length > 10 || (results[0] && Object.keys(results[0]).length > 5);

    const downloadButton = () => {
        if (results.length === 0) {
            return null;
        }
    
        return (
            <button className="download-button" onClick={downloadJsonData}>
                Data
            </button>
        );
    };    

    const completionSkeleton = () => {
        return (
            <div>
                <Skeleton width={400} height={20} />
                <Skeleton width={300} height={20} />
                <Skeleton width={100} height={20} />
                <Skeleton width={200} height={20} />
                <Skeleton width={600} height={20} />
                <Skeleton width={100} height={20} />
            </div>
        )
    }

    return (
        <div>
            <div className="search-container">
                <h1 className="search-title">BlockSearch</h1>
                <div className="search-bar-container">
                    <input
                        type="text"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        onKeyPress={handleKeyPress}
                        placeholder=""
                        className="search-bar"
                    />
                    {!query && <span className="search-bar-placeholder"></span>}
                </div>
            </div>
            <div className="results-container">
                <div className="completion-block">
                    {loading ? completionSkeleton() : (
                        completion ? (
                            <div>
                                <h4 className='completion-title'>Results</h4>
                                <p className="completion">{completion}</p>
                                {downloadButton()}
                            </div>
                        ) : null
                    )}
                </div>
            </div>
        </div>
    );
};

export default SearchPage;