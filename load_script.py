import gensim.downloader as api
from src.analogy_tests import (
    run_analogy_test_suite,
    print_test_summary
)
model = api.load('word2vec-google-news-300')

results = run_analogy_test_suite(model)
print_test_summary(results)