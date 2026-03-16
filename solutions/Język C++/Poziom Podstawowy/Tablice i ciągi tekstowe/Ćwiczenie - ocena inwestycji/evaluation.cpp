int get_evaluation( int evaluation[15][3] )
{
    int score_lok1 = 0;
    int score_lok2 = 0;
    
    for(int x = 0; x < 15;x++)
    {
       score_lok1 += evaluation[x][0] * evaluation[x][2];
       score_lok2 += evaluation[x][1] * evaluation[x][2];
       
    }
    
    float total_score1 = score_lok1; 
    float total_score2 = score_lok2; 
    
    
    if(total_score1 > total_score2 ) return 1;
    if(total_score1 < total_score2 ) return 2;
    if(total_score1 == total_score2 ) return 0;
}
