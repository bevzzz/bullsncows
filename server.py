# Third-party libraries
import uvicorn

# Local libraries
from src.server.app.api import app


if __name__ == "__main__":
    uvicorn.run(app)
