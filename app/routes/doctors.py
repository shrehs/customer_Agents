from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_doctors():
    # Return a dummy list of doctors or query your database here
    return {"doctors": ["Dr. Smith", "Dr. Jones"]}
