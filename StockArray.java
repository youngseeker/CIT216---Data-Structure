// Save this in your Notion Card
public class StockArray {
    public static void main(String[] args) {
        // Declaring the 2D array for the TMA
        // 100 Items (rows), 20 Locations (cols)
        int[][] stockData = new int[100][20];

        // Example: Storing 50 units of "Item 1" at "Location 5"
        // Note: Arrays start at index 0, so Item 1 is index 0
        stockData[0][4] = 50;

        System.out.println("Item 1 count at Location 5: " + stockData[0][4]);
    }
}