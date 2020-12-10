package day4;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class first {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("./day4/input.txt"));
        in.useDelimiter("\n\n");
        PrintWriter out = new PrintWriter("./day4/filteredinput.txt");
        ArrayList<String[]> passports = new ArrayList<>();
        HashSet<String> validFields = new HashSet<>();
        {
            validFields.add("byr");
            validFields.add("iyr");
            validFields.add("eyr");
            validFields.add("hgt");
            validFields.add("hcl");
            validFields.add("ecl");
            validFields.add("pid");
            validFields.add("cid");
        }
        int numValidPassports = 0;

        while (in.hasNext()) {
            passports.add(in.next().split("(\s|\n)"));
        }

        for (String[] passport : passports) {
            boolean isValidPassport = true;
            if (passport.length < 7) {
                continue;
            } else if (passport.length == 7) {
                for (String field : passport) {
                    if ("cid".equals(field.substring(0, 3))) {
                        isValidPassport = false;
                        break;
                    }
                }
            } else {
                for (String field : passport) {
                    if (!validFields.contains(field.substring(0, 3))) {
                        isValidPassport = false;
                        break;
                    }
                }
            }

            if (isValidPassport) {
                for (String field : passport) {
                    out.print(field + " ");
                }
                out.println();
            }
        }
        System.out.println(numValidPassports);
        in.close();
        out.close();
    }
}
