import spacy
from negspacy.negation import Negex
from negspacy.termsets import termset
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

negation_router = APIRouter(prefix="/negation", tags=["negation"])

nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler")

negex = nlp.add_pipe(
    "negex",
    # config={
    #     "neg_termset":ts.get_patterns()
    # }
)


class PatternsListModel(BaseModel):
    patterns: List[str]


@negation_router.post("/add_patterns")
async def add_patterns(patterns: PatternsListModel):
    # global ruler
    ruler.add_patterns([{"label": "MY LABEL", "pattern": pattern} for pattern in patterns.patterns])
    print(ruler.labels)
    return 'Success'


@negation_router.get('/get_negation_classification')
def get_negation_classification(sentence: str, word: str):
    doc = nlp(sentence)
    for e in doc.ents:
        if e.text == word:
            return not e._.negex


@negation_router.get('/get_all_negation_classifications')
def get_all_negation_classifications(sentence: str):
    doc = nlp(sentence)
    result = {}
    for e in doc.ents:
        result[e.text] = not e._.negex
    return result
