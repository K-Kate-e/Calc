from typing import Literal, Annotated
from fastapi import FastAPI, Query
from operations import CalcOperations

app = FastAPI()


@app.get("/calculator")
def calculator(num1: Annotated[float, Query(description="First number in expression")],
               num2: Annotated[float, Query(description="Second number in expression")],
               operation: Annotated[Literal["a", "s", "m", "d"], Query(
                    description="Available operations: a-addition, s-subtraction, "
                                "m-multiplication and d-division")]):
    res = CalcOperations(num1, num2, operation)
    return {'result': res.math_expression()}
