// Write your functions below...

Triangle createTriangle( Point p1, Point p2 ,Point p3)
{
    return Triangle{p1,p2,p3};
}

Triangle createTriangle(float ax, float ay, float bx, float by, float cx, float cy) {
    return Triangle{{ax, ay}, {bx, by}, {cx, cy}};
}