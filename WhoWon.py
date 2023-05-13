
# - If one team beat the other, print:
#     "[winner] beat [loser] by [margin]"
# - If neither team won, print:
#     "[team_1] played [team_2] and it was a tie"

team_1 = "Georgia Tech"
team_1_score = 28
team_2 = "Georgia"
team_2_score = 27

if team_1_score > team_2_score:
    winner = team_1
    loser = team_2
    margin = team_1_score - team_2_score
    print(winner, "beat", loser, "by", margin)
elif team_2_score > team_1_score:
    winner = team_2
    loser = team_1
    margin = team_2_score - team_1_score
    print(winner, "beat", loser, "by", margin)
elif team_1_score == team_2_score:
    print(team_1, "played", team_2, "and it was a tie")  

    
    


