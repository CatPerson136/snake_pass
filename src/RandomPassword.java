// This will import the random library
import java.util.Random;

// This will call the array library
import java.util.Arrays;

// This is the start of the class
public class RandomPassword {
    // This starts the Random class and makes it public
    public static Random random = new Random();
    public static void main(String[] args) {
        // This is the begining of the file.
        // System.out.println("File started"); // This is to check if the file is running
        // Function to make a random string 
        randomInt(); // This is the function that is called to genrate a random integer
    }
    public static void randomInt() {
       int randomInt = random.nextInt(20); // This will genrate a random int with a maxium value of 6
       System.out.println(randomInt);
    }
    // TODO: This will genrate a random string
    public static void randomString() {
        
    }
    // TODO: This will add to an array
    public static void addToArray() {
        
    }
}