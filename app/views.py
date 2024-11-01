from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


def movies_news(request):
    newsname="movies"
    user1="maharshi super hit"
    user2="ka super hit movie"
    user3="pushpa new look"
    types="movies"
    d={"newsname":newsname,"user1":user1,"user2":user2,"user3":user3,"types":types}
    return render(request,"news.html",d)



def sports_news(request):
    newsname="sports"
    user1="virt kohli hited 100 centuries"
    user2="india won the t20 world cup"
    user3="india won the 7 olympic medals"
    types="sports"
    d={"newsname":newsname,"user1":user1,"user2":user2,"user3":user3,"types":types}
    return render(request,"news.html",d)


def politics_news(request):
    newsname="politics"
    user1='''Karnataka Deputy Chief Minister D K Shivakumar said his statement on Shakti scheme was distorted
      and presented as if the Congress government in the state wanted to withdraw it.Shivakumars reaction came after Congress national president Mallikarjun Kharge subtly pulled 
    him in public for his statement that some women wished to pay for travelling in the buses.Whatever statement I had made was distorted as if we would stop it (Shakti scheme). I only said some section of people is saying so. There is no question of winding up any guarantee, the Deputy CM told reporters here'''
    user2='''The Deputy CM slammed the opposition parties for making a fuss about it.

"Politics is important for the opposition parties. They could not introduce such schemes and now they are unable to tolerate it. Playing with emotions, clashes, fights between parents, siblings and in-laws is their job and not the development of the state is their (BJP) politics," Shivakumar said'''
    user3='''Kharge on Thursday said, "You have given some guarantees. After seeing them, I too said in Maharashtra that there are five guarantees in Karnataka. Now you (Shivakumar) said you will withdraw one guarantee."'''
    types="politics"
    d={"newsname":newsname,"user1":user1,"user2":user2,"user3":user3,"types":types}
    return render(request,"news.html",d)