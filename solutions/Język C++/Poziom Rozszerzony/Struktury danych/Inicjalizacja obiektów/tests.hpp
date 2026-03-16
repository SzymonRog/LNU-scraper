#include <Shapes.hpp>
#include <app.cpp>

TEST(CheckIfFunctionsExist, callUsingPoints)
{
	Triangle t = createTriangle(
		Point{1, 2},
		Point{3, 4},
		Point{5, 6}
	);
	// Brak błędu -> ok
}

TEST(CheckIfFunctionsExist, callUsingNumbers)
{
	Triangle t = createTriangle(
		1, 2,
		3, 4,
		5, 6
	);
	// Brak błędu -> ok
}