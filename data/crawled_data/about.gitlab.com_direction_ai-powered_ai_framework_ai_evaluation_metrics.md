#  AI Evaluation Metrics 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Stage Direction - AI-powered](https://about.gitlab.com/direction/ai-powered/)
  4. [Group Direction - AI Framework](https://about.gitlab.com/direction/ai-powered/ai_framework/)
  5. [Category Direction - AI Evaluation](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/)
  6. AI Evaluation Metrics


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## Validation Metrics[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/metrics/#validation-metrics)
The Centralized Evaluation Framework is based on three main elements: a prompt library, an established ground truth, and validation metrics. Validation metrics assess the accuracy and usefulness of GenAI outputs against ground truth.
The Centralized Evaluation Framework incorporates various validation metrics, including but not limited to similarity scores, cross similarity scores, and LLM evaluator scores such as LLM consensus filtering and LLM judges. The combined output of use-case specific metrics serves as a proxy for production and mimics human judgment in accepting or rejecting AI-generated content.
### Similarity Scores[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/metrics/#similarity-scores)
Similarity scores compare AI-generated text against ground truth text. This ground truth may be static or may be the dynamic output of an LLM with known good answers in a specific domain.
Both the output to be tested and the ground truth are converted into numerical representations using embeddings. Embeddings are vector representations of words or sentences in a high-dimensional space, where semantically similar texts are positioned closer together. To calculate the embedding of each block, we use Vertex AI's text-embedding-gecko model. The similarity score is then calculated using the dot product of the two embeddings.
![Semantic Similarity](https://about.gitlab.com/images/direction/data-science/semantic_similarity.png)
While similarity scores are good general quality indicators, they suffer from the partial matching problem. The similarity score can only measure similarity by treating the block of text as a whole. It therefore returns a low score when the lengths of the two blocks differ significantly. When two blocks of text match partially, the similarity score will be low. Because of this, similarity scores can be misleading in cases where partial matches may still be high quality.
Examples from the code suggestion use case include:
  * The suggested code successfully matches the remainder of the function but continues to suggest a new function. In this case, we should still consider the suggestion high quality
  * The suggested code is shorter than the developer's written code, but the suggested content is a near-perfect match. The suggestion may be short due to model output token limits or because the developer-written code contains extensive logging or comments
  * The suggested code is shorter than the developer-written code, but only because the developer's code includes logging, printing, or comments between functional code segments. The functional code itself is a near-perfect match


### Cross Similarity Score[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/metrics/#cross-similarity-score)
The cross similarity score overcomes the partial matching problem, allowing us to better evaluate text produced by GenAI across multiple use cases.
The cross similarity score is based on a cross similarity matrix, which compares element pairs across two outputs and quantifies the similarity or dissimilarity of each element. A matrix is constructed with rows and columns representing the relationship and similarity score of each element in one output to each element in another output. The scores are then aggregated to obtain a single score representing the overall similarity between two outputs.
![Cross Similarity Score](https://about.gitlab.com/images/direction/data-science/cross_similarity_score.png)
### LLM Judge[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/metrics/#llm-judge)
The LLM Judge metric assesses specific criteria, such as the relevance of a response to a question. In this approach, one LLM (the LLM Judge) rates the responses of the LLM being evaluated against a series of prompts. The LLM Judge then scores these responses for specific criteria such as correctness, comprehensiveness, and readability.
To enhance credibility, we employ multiple LLMs as judges. The LLM Judges are selected based on their strong language comprehension capabilities.
### Consensus Filtering with LLM Judge[](https://about.gitlab.com/direction/ai-powered/ai_framework/ai_evaluation/metrics/#consensus-filtering-with-llm-judge)
Consensus filtering with an LLM Judge compares outputs from multiple LLMs responding to the same set of prompts. Unlike the single LLM Judge approach, this method aggregates all LLM outputs into a single prompt. The LLM Judge then compares the different responses and scores each one with full context of the range of possible answers.
![LLM Judge](https://about.gitlab.com/images/direction/data-science/LLM_judge.png)
_  
Last Reviewed: 2025-06-11  
Last Updated: 2025-06-11 _
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/ai-powered/ai_framework/ai_evaluation/metrics/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/ai-powered/ai_framework/ai_evaluation/metrics/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fai-powered%2Fai_framework%2Fai_evaluation%2Fmetrics%2F&_biz_t=1773332128058&_biz_i=%0AAI%20Evaluation%20Metrics%0A%7C%0AGitLab%0A&_biz_n=126&rnd=522343&cdn_o=a&_biz_z=1773332128180)
suggested results