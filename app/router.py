from semantic_router import Route, RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount witht the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",

    ]
)


sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are ther any Puma shoes on sale?",
        "What is the price of puma running shoes"
    ]
)


small_talk = Route(
    name='small-talk',
    utterances=[
        "Hi there",
        "Good morning",
        "Hello?",
        "Is any one there",
        "Hi? is can you help me?",
        "excuse me?",
        "anyone here to help?",
        "Thank you",
        "okay thanks",
        "bye",
        "No"
    ]
)

router = RouteLayer(routes=[faq, sql, small_talk], encoder=encoder)


if __name__ == "__main__":
    print(router("anyone here to help?").name)
    print(router("Any shoes with price range of 5000 to 10000").name)
