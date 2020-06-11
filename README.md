# nlp-bert
A project with a variaty of Natural Language Proccessing problems

## Question and Answer
`questionanswer.indexed_question.py` implements a QA based on Google’s BERT language model using Keras + Tensorflow wrapped by the KTrain (project intent to avoid boilerplate code when using keras).

### How to use
- Run rest-api.
- Access the browser and ask a question following the pattern:
Question: When Cassini was launched?
http://localhost:8080/ask/when%20Cassini%20was%20launched
A JSON string is expected.

`[{
    "answer": "2001", 
    "confidence": 0.35825988818742366, 
    "context": "o mars rover sample return (mrsr) robotics rover would return samples of mars ' atmosphere and surface to earch for analysis. possible launch dates : 1996 for imaging orbiter, 2001 for rover."
  },
  ...
]
`

It allows us to open to questions a text knowledge-base e.g: Confluence, PDFs, Help Pages etc.