import json

from pydantic_logic import Logic, LogicExpression, Operator

data = {
    "Phone number": "123123123",
    "some_value": True,
    "some_other_value": 1,
}

logic = Logic(
    expressions=[
        LogicExpression.b("Phone number", Operator.EQ, "123123123"),
        LogicExpression.b("some_value", Operator.NE, False),
        LogicExpression.b("some_other_value", Operator.LT, 1),
    ]
)
assert not logic.evaluate(data)


logic = Logic(
    expressions=[
        LogicExpression.b("Phone number", Operator.NE, "adasdasdasd"),
        LogicExpression.b("some_value", Operator.EQ, True),
        LogicExpression.b("some_other_value", Operator.GT, 0),
    ]
)
assert logic.evaluate(data)

print(json.dumps(logic.model_dump(mode="json"), indent=2, ensure_ascii=False))
