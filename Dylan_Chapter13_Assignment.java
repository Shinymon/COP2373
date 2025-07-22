package ch13;

import java.util.InputMismatchException;
import java.util.Scanner;

// Main class with the main method
public class Dylan_Chapter13_Assignment {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        try {
            // RECTANGLE INPUT
            System.out.println("Enter length and width for rectangle:");
            double length = input.nextDouble();
            double width = input.nextDouble();
            input.nextLine(); // consume leftover newline

            // Get color and filled status
            System.out.println("Enter color:");
            String color = input.nextLine();
            System.out.println("Is the rectangle filled? (true/false):");
            boolean filled = input.nextBoolean();

            // Create rectangle object
            rectangle_DT rect = new rectangle_DT(length, width);
            rect.setColor(color);
            rect.setFilled(filled);

            // === CIRCLE INPUT ===
            System.out.println("\nEnter radius for circle:");
            double radius = input.nextDouble();
            input.nextLine(); // consume leftover newline

            System.out.println("Enter color:");
            color = input.nextLine();
            System.out.println("Is the circle filled? (true/false):");
            filled = input.nextBoolean();

            // Create circle object
            circle_DT circ = new circle_DT(radius);
            circ.setColor(color);
            circ.setFilled(filled);

            // TRIANGLE INPUT
            System.out.println("\nEnter three sides for triangle:");
            double s1 = input.nextDouble();
            double s2 = input.nextDouble();
            double s3 = input.nextDouble();
            input.nextLine(); // consume leftover newline

            System.out.println("Enter color:");
            color = input.nextLine();
            System.out.println("Is the triangle filled? (true/false):");
            filled = input.nextBoolean();

            // Create triangle object
            triangle_DT tri = new triangle_DT(s1, s2, s3);
            tri.setColor(color);
            tri.setFilled(filled);

            // DISPLAY INFO FOR EACH SHAPE
            System.out.println("\n--- Rectangle Info ---");
            displayInfo(rect);

            System.out.println("\n--- Circle Info ---");
            displayInfo(circ);

            System.out.println("\n--- Triangle Info ---");
            displayInfo(tri);

            // Create polymorphic references to GeometricObject
            GeometricObject obj1 = rect;
            GeometricObject obj2 = circ;
            GeometricObject obj3 = tri;

            // Compare area of rectangle and circle
            System.out.println("\nRectangle and Circle have same area? " + equalArea(obj1, obj2));

            // Compare perimeters
            System.out.println("Rectangle vs Circle perimeter equal? " + equalPerimeter(obj1, obj2));
            System.out.println("Rectangle vs Triangle perimeter equal? " + equalPerimeter(obj1, obj3));
            System.out.println("Circle vs Triangle perimeter equal? " + equalPerimeter(obj2, obj3));

        } catch (InputMismatchException e) {
            // Handle invalid input like strings where numbers are expected
            System.out.println("Invalid input. Please enter correct data types.");
        } catch (IllegalArgumentException e) {
            // Handle invalid geometric object creation (like negative sides)
            System.out.println("Invalid geometric values: " + e.getMessage());
        } finally {
            input.close(); // Always close Scanner
        }
    }

    // Method to display geometric object details
    public static void displayInfo(GeometricObject obj) {
        System.out.println("Color: " + obj.getColor());
        System.out.println("Filled: " + obj.isFilled());
        System.out.println("Perimeter: " + obj.getPerimeter());

        // Only rectangle and circle have simple area formulas, show area
        if (obj instanceof rectangle_DT || obj instanceof circle_DT) {
            System.out.println("Area: " + obj.getArea());
        }
    }

    // Method to compare the area of two GeometricObject instances
    public static boolean equalArea(GeometricObject o1, GeometricObject o2) {
        return Double.compare(o1.getArea(), o2.getArea()) == 0;
    }

    // Method to compare the perimeter of two GeometricObject instances
    public static boolean equalPerimeter(GeometricObject o1, GeometricObject o2) {
        return Double.compare(o1.getPerimeter(), o2.getPerimeter()) == 0;
    }
}

// rectangle_DT class
class rectangle_DT extends GeometricObject {
    private double width;
    private double height;

    // Constructor with validation
    public rectangle_DT(double width, double height) {
        if (width <= 0 || height <= 0)
            throw new IllegalArgumentException("Width and height must be positive.");
        this.width = width;
        this.height = height;
    }

    // Return area of rectangle
    @Override
    public double getArea() {
        return width * height;
    }

    // Return perimeter of rectangle
    @Override
    public double getPerimeter() {
        return 2 * (width + height);
    }
}

// circle_DT class
class circle_DT extends GeometricObject {
    private double radius;

    // Constructor with validation
    public circle_DT(double radius) {
        if (radius <= 0)
            throw new IllegalArgumentException("Radius must be positive.");
        this.radius = radius;
    }

    // Return area of circle
    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }

    // Return perimeter (circumference) of circle
    @Override
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }
}

// triangle_DT class
class triangle_DT extends GeometricObject {
    private double side1, side2, side3;

    // Constructor with validation using triangle inequality
    public triangle_DT(double s1, double s2, double s3) {
        if (s1 + s2 <= s3 || s1 + s3 <= s2 || s2 + s3 <= s1)
            throw new IllegalArgumentException("Invalid triangle sides.");
        this.side1 = s1;
        this.side2 = s2;
        this.side3 = s3;
    }

    // Return area using Heron's formula
    @Override
    public double getArea() {
        double s = getPerimeter() / 2;
        return Math.sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }

    // Return perimeter of triangle
    @Override
    public double getPerimeter() {
        return side1 + side2 + side3;
    }
}

// GeometricObject abstract class
abstract class GeometricObject {
    private String color = "white"; // default color
    private boolean filled;

    // Abstract methods to be implemented in subclasses
    public abstract double getArea();
    public abstract double getPerimeter();

    // Getter/setter for color
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    // Getter/setter for filled
    public boolean isFilled() {
        return filled;
    }

    public void setFilled(boolean filled) {
        this.filled = filled;
    }
}