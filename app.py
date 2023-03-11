import sanic
import logging
from sanic_cors import CORS

app = sanic.Sanic('data-analysis-project-01')
CORS(app)
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s'
)


@app.get('/server')
async def server(request):
    return sanic.response.json({"message": "server : on"}, 200)

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=3000,
        debug=False,
        access_log=True,
        auto_reload=True,
        dev=True
    )
