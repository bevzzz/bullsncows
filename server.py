# Third-party libraries
import uvicorn

# Local libraries
from server.app.api import app


if __name__ == "__main__":
    uvicorn.run(app, port=9000)
