word="python"
list=["_"]*len(word)
print("pick a letter")
ans=input()
if ans in word:
    for i in range(len(word)):
        if word[i]==ans:
            list [i]=ans
print(" ".join(list))