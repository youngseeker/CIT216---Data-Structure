import java.util.HashMap;

// 1. First, we need our blueprint for the variable information
class SymbolInfo {
    String type;
    String scope;
    String memoryAddress;

    public SymbolInfo(String type, String scope, String memoryAddress) {
        this.type = type;
        this.scope = scope;
        this.memoryAddress = memoryAddress;
    }

    public String toString() {
        return "[Type: " + type + " | Scope: " + scope + " | Address: " + memoryAddress + "]";
    }
}

// 2. Now the actual program
public class CompilerSymbolTable {
    public static void main(String[] args) {
        HashMap<String, SymbolInfo> symbolTable = new HashMap<>();

        // 3. The compiler reads: int age = 19;
        symbolTable.put("age", new SymbolInfo("int", "global", "0x00A1"));

        // 4. The compiler reads a new line: String age = "Daniel";
        // It's trying to declare 'age' again!
        String newVariableToRead = "age";

        // 5. The Hash Table Error Check:
        System.out.println("Checking code for errors...\n");
        
        if (symbolTable.containsKey(newVariableToRead)) {
            // It instantly knows "age" is already taken!
            System.out.println("COMPILER ERROR: Variable '" + newVariableToRead + "' is already defined!");
            System.out.println("Existing details: " + symbolTable.get(newVariableToRead));
        } else {
            symbolTable.put(newVariableToRead, new SymbolInfo("String", "local", "0x00B2"));
            System.out.println("Variable saved successfully.");
        }
    }
}