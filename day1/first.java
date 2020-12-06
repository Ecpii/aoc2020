package day1;

import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

class first {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("./day1/input.txt"));
        ArrayList<Integer> numbers = new ArrayList<>();

        while (in.hasNext()) {
            numbers.add(in.nextInt());
        }

        for (int i = 0; i < numbers.size() - 1; i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (numbers.get(j) + numbers.get(i) == 2020) {
                    System.out.println(numbers.get(j) * numbers.get(i));
                    in.close();
                    break;
                }
            }
        }
    }
}