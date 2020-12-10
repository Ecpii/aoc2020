package day3;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class first {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("./day3/input.txt"));
        ArrayList<String> hill = new ArrayList<>();
        int treesEncountered = 0;

        while (in.hasNext()) {
            hill.add(in.nextLine());
        }
        int sectionLength = hill.get(0).length();

        for (int row = 1; row < hill.size(); row++) {
            int col = (row * 3) % sectionLength;
            // print statements are debugging
            if (row < 20) {
                System.out.println("Row " + (row + 1) + " - Col " + (col + 1));
                System.out.println("@@ char: " + hill.get(row).charAt(col));
                System.out.println("Hill: ");
                System.out.println(hill.get(row) + hill.get(row) + hill.get(row));
            }
            if (hill.get(row).charAt(col) == '#') {
                System.out.println("---- tree found!");
                treesEncountered++;
            }
        }

        System.out.println(treesEncountered);
    }
}
