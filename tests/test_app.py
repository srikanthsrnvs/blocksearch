def test_query_bigquery_no_query(client):
    response = client.get('/')
    assert response.status_code == 400
    assert response.json == {'error': 'Missing query parameter'}

def test_query_bigquery(client, mocker):
    mocker.patch('openai.Completion.create', return_value=FakeOpenAIAPIResponse())
    mocker.patch('google.cloud.bigquery.Client.query', return_value=FakeBigQueryJobResult())

    response = client.get('/', query_string={'query': 'Show me the last 20 USDC transfers'})
    assert response.status_code == 200
    assert response.json == [{'total_sales': 1000}]

class FakeOpenAIAPIResponse:
    def __init__(self):
        self.choices = [FakeOpenAIAPIChoice()]

class FakeOpenAIAPIChoice:
    def __init__(self):
        self.text = 'SELECT SUM(sales) as total_sales FROM sales WHERE date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH);'

class FakeBigQueryJobResult:
    def result(self):
        return [FakeBigQueryRow()]

class FakeBigQueryRow:
    def items(self):
        return [('total_sales', 1000)]
