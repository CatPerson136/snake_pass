// This is the start of the class
public class RandomPassword {
    /*
     * Thanks to Geeks or Geeks for the code.
     * The code can be found here:
     * https://www.geeksforgeeks.org/generate-random-string-of-given-size-in-java/
     * I also modfiyed it to work in here.
     */
    static String getAlphaNumericString(int n) {
        // choose a Character random from this String
        String AlphaNumericString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                + "0123456789"
                + "abcdefghijklmnopqrstuvxyz"
                + "!@#$%^&*{}:w?";
        // create StringBuffer size of AlphaNumericString
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            // generates a random number between
            // 0 to AlphaNumericString variable length
            int index = (int) (AlphaNumericString.length() * Math.random());
            // add Character one by one in end of sb
            sb.append(AlphaNumericString.charAt(index));
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        // Gets the string function add displays it
        System.out.println(RandomPassword.getAlphaNumericString(30));
    }
}