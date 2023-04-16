// This is where the files are.
package cat;

// This will be the import of py4j gateway server. 
import py4j.GatewayServer;

// This is the start of the class
public class RandomPassword {
    /*
     * Thanks to Geeks or Geeks for the code.
     * The code can be found here:
     * https://www.geeksforgeeks.org/generate-random-string-of-given-size-in-java/
     * I also modfied it to add other characters as.
     */
    static String getAlphaNumericString(int n) {
        // Choose a Character random from this String
        String passStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                + "0123456789"
                + "abcdefghijklmnopqrstuvxyz"
                + "!@#$%^&*{}:w?";
        // Creates StringBuffer the size of AlphaNumericString
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            // Generates a random number between
            // 0 to AlphaNumericString variable length
            int index = (int) (passStr.length() * Math.random());
            // Add character one by one in end of sb
            sb.append(passStr.charAt(index));
        }
        return sb.toString();
    }

    public static void printPass() {
        // This is the gateway needed to use in the python file.
        System.out.println(RandomPassword.getAlphaNumericString(30));
    }

    public static void main(String[] args) {
        // This will start the gateway server with a custom port of 69420.
        GatewayServer gs = new GatewayServer(new RandomPassword(), 69420);
        // This will start the server.
        gs.start();
        printPass();
    }
}