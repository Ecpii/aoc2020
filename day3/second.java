package day3;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class second {
    public static void main(String[] args) throws IOException {
        long result = countTrees(1, 1);
        result *= countTrees(3, 1);
        result *= countTrees(5, 1);
        result *= countTrees(7, 1);
        System.out.println(result * countTrees(1, 2));
    }

    public static int countTrees(int... slope) throws IOException  {
        Scanner in = new Scanner(new File("./day3/input.txt"));
        ArrayList<String> hill = new ArrayList<>();
        int treesEncountered = 0;

        while (in.hasNext()) {
            hill.add(in.nextLine());
        }
        int sectionLength = hill.get(0).length();

        for (int row = slope[1]; row < hill.size(); row += slope[1]) {
            int col = (row / slope[1] * slope[0]) % sectionLength;
            // print statements are debugging
            if (row < 10) {
                System.out.println("Row " + (row + 1) + " - Col " + (col + 1));
                System.out.println("@@ char: " + hill.get(row).charAt(col));
                System.out.println("Hill: ");
                System.out.println(hill.get(row) + hill.get(row) + hill.get(row));
            }
            if (hill.get(row).charAt(col) == '#') {
                treesEncountered++;
            }
        }

        return treesEncountered;
    }
}
