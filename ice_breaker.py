from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
information = """
Virat Kohli (Hindi pronunciation: [ʋɪˈɾɑːʈ ˈkoːɦli] (listen); born 5 November 1988) is an Indian international cricketer and the former captain of the Indian national cricket team who plays as a right-handed batsman for Royal Challengers Bangalore in the IPL and for Delhi in Indian domestic cricket. Widely regarded as one of the greatest batsmen of all time, and the best of his time, as well in the current era.[4] Kohli holds the records for scoring most runs in T20 internationals and in the IPL. In 2020, the International Cricket Council named him the male cricketer of the decade. Kohli has also contributed to a number of India's successes, including winning the 2011 World Cup and the 2013 Champions trophy.

Born and raised in New Delhi, Kohli trained at the West Delhi Cricket Academy and started his youth career with the Delhi Under-15 team. He made his international debut in 2008 and quickly became a key player in the ODI team and later made his Test debut in 2011. In 2013, Kohli reached the number one spot in the ICC rankings for ODI batsmen for the first time. During 2014 T20 World Cup, he set a record for the most runs scored in the tournament. In 2018, he achieved yet another milestone, becoming the world's top-ranked Test batsman, making him the only Indian cricketer to hold the number one spot in all three formats of the game. His form continued in 2019, when he became the first player to score 20,000 international runs in a single decade. In 2021, Kohli made the decision to step down as the captain of the Indian national team for T20Is, following the T20 World Cup and in early 2022 he stepped down as the captain of the Test team as well.

He has received many accolades for his performances on the cricket field. He was recognized as the ICC ODI Player of the Year in 2012 and has won the Sir Garfield Sobers Trophy, given to the ICC Cricketer of the Year, on two occasions, in 2017 and 2018 respectively. Subsequently, Kohli also won ICC Test Player of the Year and ICC ODI Player of the Year awards in 2018, becoming the first player to win both awards in the same year. Additionally, he was named the Wisden Leading Cricketer in the World for three consecutive years, from 2016 to 2018. At the national level, Kohli was honoured with the Arjuna Award in 2013, the Padma Shri under the sports category in 2017 and the Khel Ratna award, India's highest sporting honour, in 2018.

In 2016, he was ranked as one of the world's most famous athletes by ESPN, and one of the most valuable athlete brands by Forbes. In 2018, Time magazine included him on its list of the 100 most influential people in the world. In 2020, he was ranked 66th in Forbes list of the top 100 highest-paid athletes in the world for the year 2020 with estimated earnings of over $26 million. Kohli has been deemed one of the most commercially viable cricketers, with estimated earnings of ₹165 crore (US$21 million) in the year 2022.

Early life
Virat Kohli was born on 5 November 1988 in Delhi to a Punjabi Hindu family. His father, Prem Kohli, worked as a criminal lawyer and his mother, Saroj Kohli, served as a housewife. He has an older brother, Vikas, and an older sister, Bhawna.[5] Kohli's formative years were spent in the Uttam Nagar and commenced his early education at Vishal Bharti Public School.[6] According to his family, Kohli exhibited an early affinity for cricket as a mere three-year-old. He would pick up a cricket bat, display natural skill, and request his father to bowl to him.[7]

In 1998, the West Delhi Cricket Academy (WCDA) was created and on 30 May of that year, Prem Kohli, espoused his younger son's fervour for cricket, assisted nine-year-old Kohli's aspirations and arranged for him to meet Rajkumar Sharma, who initially perceived him to be just another enthusiastic and determined young boy. However, two weeks later, Sharma was impressed by Kohli's accuracy and power in throwing.[8] Upon the suggestion of their neighbours, Kohli's father considered enrolling his son in a professional cricket academy, as they believed that his cricketing abilities merited more than just playing in the gully cricket.[9] Despite his abilities, he faced the setback of being unable to secure a place in the under-14 Delhi team, not due to a lack of merit but due to extraneous factors. Prem Kohli received offers to relocate his son to influential clubs, which would have ensured his selection, but he declined the proposals, as he was determined that Kohli should earn his recognition based on his own merit and overcome the system of nepotism and deceit prevalent in the Delhi and District Cricket Association (DDCA). Kohli persisted and eventually found his way into the under-15 Delhi team.[10] He received training at the academy while simultaneously participating in matches at the Sumeet Dogra Academy located at Vasundhara Enclave.[11] As per Sharma's recollection of Kohli's initial days at his academy, he exuded remarkable talent, making it arduous for the coach to curb his enthusiasm. Kohli remained prepared to bat at any position, and often, Sharma had to physically coerce him to leave the training sessions, as he was reluctant to depart.[12] In pursuit of furthering his cricketing career, he transitioned to Saviour Convent School during his ninth-grade education.[9] Kohli's ardent passion for cricket compelled him to travel long distances with his father to ensure that he never missed a match. With time, he diligently honed his skills and diversified his range of shots, commanding respect from the local bowlers.[13]

On the 18th of December 2006, Kohli experienced the loss of his father due to a cerebral attack.[9][14] During his childhood, his father played a crucial role in supporting his cricket training. Kohli has credited his father as the one who drove him to practice every day. He has expressed his feelings of missing his father's presence at times.[6][15] Following the demise of Kohli's father, his mother observed a significant change in his personality. Kohli appeared to become more mature overnight, and he began taking every cricket match seriously. He harboured an aversion to exclusion from games and appeared to channel his entire existence into the pursuit of cricket following his father's untimely demise.[9] Kohli's family resided in Meera Bagh, Paschim Vihar until the year 2015, after which they relocated to Gurgaon.[16
"""

if __name__ == "__main__":
    print("Hello Langchain")

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    #print(chain.run(information=information))

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/rishav-goutam-soam/')
    print(chain.run(information=linkedin_data))
