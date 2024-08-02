{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b3cb3908-5d2b-4bce-b900-df33be84dec8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import nltk\n",
    "from nltk.tokenize import word_tokenize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "745963dc-fc44-463a-9017-27443c55d1ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sample text\n",
    "text = \"John Doe is the CEO of OpenAI. He lives in San Francisco.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8241157d-0b79-4514-a849-f764e6f8a462",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Lexicons for different entity types\n",
    "person_lexicon = {\"John Doe\", \"Alice\", \"Bob\"}\n",
    "organization_lexicon = {\"OpenAI\", \"Google\", \"Microsoft\"}\n",
    "location_lexicon = {\"San Francisco\", \"New York\", \"Los Angeles\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f40ae587-b26e-44e7-bdad-5ef73f4d829d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lexicon-based NER:\n",
      "[('OpenAI', 'ORG')]\n"
     ]
    }
   ],
   "source": [
    "def lexicon_based_ner(text):\n",
    "    entities = []\n",
    "    tokens = word_tokenize(text)\n",
    "    for token in tokens:\n",
    "        if token in person_lexicon:\n",
    "            entities.append((token, \"PERSON\"))\n",
    "        elif token in organization_lexicon:\n",
    "            entities.append((token, \"ORG\"))\n",
    "        elif token in location_lexicon:\n",
    "            entities.append((token, \"LOC\"))\n",
    "    return entities\n",
    "\n",
    "print(\"Lexicon-based NER:\")\n",
    "print(lexicon_based_ner(text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed14f529-d9a6-439e-8ab4-4dd1d2b28c3d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
