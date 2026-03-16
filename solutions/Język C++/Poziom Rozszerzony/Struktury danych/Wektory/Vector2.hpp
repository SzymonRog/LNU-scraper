// Umieść definicję struktury i nadpisanie operatorów tutaj
#pragma once

struct Vector2{
    double x,y;
    
     Vector2 operator+(const Vector2& other) const {
        return Vector2(x + other.x, y + other.y);
    }

    // Operator odejmowania dwóch wektorów
    Vector2 operator-(const Vector2& other) const {
        return Vector2(x - other.x, y - other.y);
    }

    // Operator mnożenia wektora przez skalar
    Vector2 operator*(double scalar) const {
        return Vector2(x * scalar, y * scalar);
    }
    
    friend Vector2 operator*(double scalar, const Vector2& v) {
        return v * scalar; // Korzystamy z operatora * wewnętrznego
    }

    // Operator iloczynu skalarnego dwóch wektorów
    double operator*(const Vector2& other) const {
        return x * other.x + y * other.y;  // Iloczyn skalarny
    }
};