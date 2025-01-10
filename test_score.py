#score={"score":0}
with open("score.txt","r+") as f:
    load_score=int(f.read())
val=0
for i in range(5):

    load_score=load_score+1
    print(load_score)

with open("score.txt","w+") as file:
    new_score=load_score
    file.write(str(new_score))