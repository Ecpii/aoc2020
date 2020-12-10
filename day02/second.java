package day2;

import java.io.File;
import java.util.Scanner;
import java.io.IOException;

public class second {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("./day2/input.txt"));
        int validPasswords = 0;

        while (in.hasNext()) {
            String passwordLine = in.nextLine();

            int hyphenIndex = passwordLine.indexOf('-');
            int firstIndex = Integer.parseInt(passwordLine.substring(0, hyphenIndex));
            passwordLine = passwordLine.substring(hyphenIndex + 1);

            int spaceIndex = passwordLine.indexOf(' ');
            int secondIndex = Integer.parseInt(passwordLine.substring(0,  spaceIndex));
            passwordLine = passwordLine.substring(spaceIndex + 1);

            char desiredChar = passwordLine.charAt(0);
            String password = passwordLine.substring(passwordLine.indexOf(' ') + 1);

            char firstChar = password.charAt(firstIndex - 1);
            char secondChar = password.charAt(secondIndex - 1);

            if ((firstChar == desiredChar) ^ (secondChar == desiredChar)) {
                validPasswords++;
            }
        }
        System.out.println(validPasswords);
    }
}
