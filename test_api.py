import requests

def test_status_code():
    """Test that the API returns a successful status code."""
    url = "https://opentdb.com/api.php?amount=10"
    response = requests.get(url)
    assert response.status_code == 200
    print("✅ Status code test passed!")
    
    # Print some basic info about the response
    data = response.json()
    print(f"📊 Response keys: {list(data.keys())}")
    print(f"📊 Response code: {data.get('response_code', 'Not found')}")
    
    if 'results' in data:
        print(f"📊 Number of questions: {len(data['results'])}")
        print("\n🔍 First 5 questions:")
        print("=" * 60)
        
        for i, question in enumerate(data['results'][:5], 1):
            print(f"\n{i}. Question: {question.get('question', 'No question')}")
            print(f"   Category: {question.get('category', 'No category')}")
            print(f"   Difficulty: {question.get('difficulty', 'No difficulty')}")
            print(f"   Correct Answer: {question.get('correct_answer', 'No answer')}")
            print(f"   Incorrect Answers: {question.get('incorrect_answers', [])}")
            print("-" * 40)
    else:
        print("❌ No 'results' key found in response")
        print(f"📊 Full response: {data}")

def main():
    """Run the simplified test."""
    print("🧪 Testing Open Trivia Database API...")
    print("=" * 50)
    
    try:
        test_status_code()
        print("=" * 50)
        print("🎉 Basic API test completed!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main() 