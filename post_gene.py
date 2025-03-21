from LLM_helper import llm
from few_shot import FewShotPosts

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    
def get_prompt(length,language,tag):
    length_str=get_length_str(length)

    few_shot = FewShotPosts()
    prompt = f'''
    Generate a Linkdin post using the below information. No Preamble.

    1) Topic: {tag}
    2) Length: {length}
    3) Language: {language}
    The script for the generated post should always be in English


    '''
    examples = few_shot.get_filtered_posts(length,language,tag)
    
    for i , post in enumerate(examples):
        post_text = post['text']
        prompt += f"\n\n Example{i+1}: \n\n {post_text}"
        if i ==1 :
            break;
    return prompt
   
    


def generate_post(length, language, tag):
     from LLM_helper import llm  # Moved inside the function
     from few_shot import FewShotPosts  # Moved inside the function
     prompt = get_prompt(length,language,tag)
     response =llm.invoke(prompt)
     return response.content
    

if __name__ == "__main__":
    post = generate_post("Short","English","Self Improvement")
    print(post)