// Niestety coraz częściej pliki będą puste :/
void moveTimeByMin(unsigned int& h, unsigned int& min, unsigned int moveBy){
     unsigned int totalMin = (h * 60) + min + moveBy;
    h = (totalMin/60) % 24;
    min = (totalMin % 60);
}