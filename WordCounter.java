import java.util.HashMap;

public class WordCounter {

    // The main method is the entry point so you can run the file
    public static void main(String[] args) {
        // A sample document array to test our counter
        String[] sampleDocument = {"ett", "tva", "tre", "ett", "tre", "tre"};
        
        countWords(sampleDocument);
    }

    public static void countWords(String[] document) {
        // 1. Create our standard Java hash table
        // We tell it the Key is a String (the word), and the Value is an Integer (the count)
        HashMap<String, Integer> table = new HashMap<>();

        // 2. Read through every word in the document
        for (String word : document) {
            
            // 3. Check if the word is in the table
            if (table.containsKey(word)) {
                // If it IS there, get the current count, add 1, and update it
                int currentCount = table.get(word);
                table.put(word, currentCount + 1);
            } else {
                // If it's NOT there, insert it and start the count at 1
                table.put(word, 1);
            }
        }

        // Print the final hash table to the console so you can see the results!
        System.out.println("Final Word Counts: " + table);
    }
}