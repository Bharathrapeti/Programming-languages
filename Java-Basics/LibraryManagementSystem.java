import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.util.ArrayList;
import java.util.List;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.table.DefaultTableModel;

public class LibraryManagementSystem {
    private static final String MAIN_CARD = "main";
    private static final String ADD_CARD = "add";
    private static final String SEARCH_CARD = "search";
    private static final String DELETE_CARD = "delete";

    private final List<Book> bookList = new ArrayList<>();
    private final CardLayout cardLayout = new CardLayout();
    private final JPanel cards = new JPanel(cardLayout);
    private final JFrame frame = new JFrame("Online Library Management System");

    private final JTextField titleField = new JTextField();
    private final JTextField authorField = new JTextField();
    private final JTextField isbnField = new JTextField();
    private final JTextField yearField = new JTextField();
    private final JComboBox<String> genreBox = new JComboBox<>(
            new String[]{"Fiction", "Non-Fiction", "Science", "Technology"});
    private final JTextField searchField = new JTextField();
    private final DefaultTableModel tableModel = new DefaultTableModel(
            new String[]{"Title", "Author", "ISBN", "Year", "Genre"}, 0) {
        @Override
        public boolean isCellEditable(int row, int column) {
            return false;
        }
    };
    private final JTextField deleteField = new JTextField();

    public static class Book {
        private final String title;
        private final String author;
        private final String isbn;
        private final String year;
        private final String genre;

        public Book(String title, String author, String isbn, String year, String genre) {
            this.title = title;
            this.author = author;
            this.isbn = isbn;
            this.year = year;
            this.genre = genre;
        }
    }

    public LibraryManagementSystem() {
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(650, 450);
        frame.setLocationRelativeTo(null);

        cards.add(createMainPanel(), MAIN_CARD);
        cards.add(createAddPanel(), ADD_CARD);
        cards.add(createSearchPanel(), SEARCH_CARD);
        cards.add(createDeletePanel(), DELETE_CARD);
        frame.add(cards);
    }

    private JPanel createMainPanel() {
        JPanel panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 30));
        JButton addButton = new JButton("Add Book");
        JButton searchButton = new JButton("Search Book");
        JButton deleteButton = new JButton("Delete Book");

        addButton.addActionListener(e -> showCard(ADD_CARD));
        searchButton.addActionListener(e -> showCard(SEARCH_CARD));
        deleteButton.addActionListener(e -> showCard(DELETE_CARD));

        panel.add(addButton);
        panel.add(searchButton);
        panel.add(deleteButton);
        return panel;
    }

    private JPanel createAddPanel() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        JPanel form = new JPanel(new GridLayout(5, 2, 10, 10));

        form.add(new JLabel("Book Title:"));
        form.add(titleField);
        form.add(new JLabel("Author:"));
        form.add(authorField);
        form.add(new JLabel("ISBN:"));
        form.add(isbnField);
        form.add(new JLabel("Publication Year:"));
        form.add(yearField);
        form.add(new JLabel("Genre:"));
        form.add(genreBox);

        JButton saveButton = new JButton("Save");
        JButton backButton = new JButton("Back");
        saveButton.addActionListener(e -> saveBook());
        backButton.addActionListener(e -> showCard(MAIN_CARD));

        JPanel buttons = new JPanel(new FlowLayout(FlowLayout.CENTER));
        buttons.add(saveButton);
        buttons.add(backButton);
        panel.add(form, BorderLayout.CENTER);
        panel.add(buttons, BorderLayout.SOUTH);
        return panel;
    }

    private JPanel createSearchPanel() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        JPanel top = new JPanel(new BorderLayout(10, 0));
        top.add(new JLabel("Search by title or ISBN:"), BorderLayout.WEST);
        top.add(searchField, BorderLayout.CENTER);
        JButton searchButton = new JButton("Search");
        searchButton.addActionListener(e -> searchBooks());
        top.add(searchButton, BorderLayout.EAST);

        JTable table = new JTable(tableModel);
        table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        JButton backButton = new JButton("Back");
        backButton.addActionListener(e -> showCard(MAIN_CARD));

        panel.add(top, BorderLayout.NORTH);
        panel.add(new JScrollPane(table), BorderLayout.CENTER);
        panel.add(backButton, BorderLayout.SOUTH);
        return panel;
    }

    private JPanel createDeletePanel() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        JPanel top = new JPanel(new BorderLayout(10, 0));
        top.add(new JLabel("Delete by ISBN:"), BorderLayout.WEST);
        top.add(deleteField, BorderLayout.CENTER);

        JButton deleteButton = new JButton("Delete");
        deleteButton.addActionListener(e -> deleteBook());
        JButton backButton = new JButton("Back");
        backButton.addActionListener(e -> showCard(MAIN_CARD));

        JPanel buttons = new JPanel(new FlowLayout(FlowLayout.CENTER));
        buttons.add(deleteButton);
        buttons.add(backButton);
        panel.add(top, BorderLayout.NORTH);
        panel.add(buttons, BorderLayout.SOUTH);
        return panel;
    }

    private void saveBook() {
        String title = titleField.getText().trim();
        String author = authorField.getText().trim();
        String isbn = isbnField.getText().trim();
        String year = yearField.getText().trim();
        String genre = (String) genreBox.getSelectedItem();

        if (title.isEmpty() || author.isEmpty() || isbn.isEmpty() || year.isEmpty()) {
            showMessage("Please fill in all book details.", JOptionPane.WARNING_MESSAGE);
            return;
        }

        bookList.add(new Book(title, author, isbn, year, genre));
        titleField.setText("");
        authorField.setText("");
        isbnField.setText("");
        yearField.setText("");
        genreBox.setSelectedIndex(0);
        showMessage("Book added successfully.", JOptionPane.INFORMATION_MESSAGE);
    }

    private void searchBooks() {
        String keyword = searchField.getText().trim().toLowerCase();
        tableModel.setRowCount(0);
        for (Book book : bookList) {
            if (book.title.toLowerCase().contains(keyword)
                    || book.isbn.toLowerCase().contains(keyword)) {
                tableModel.addRow(new Object[]{
                        book.title, book.author, book.isbn, book.year, book.genre
                });
            }
        }
    }

    private void deleteBook() {
        String isbn = deleteField.getText().trim();
        for (int i = 0; i < bookList.size(); i++) {
            if (bookList.get(i).isbn.equalsIgnoreCase(isbn)) {
                bookList.remove(i);
                deleteField.setText("");
                showMessage("Book deleted successfully.", JOptionPane.INFORMATION_MESSAGE);
                return;
            }
        }
        showMessage("Book not found.", JOptionPane.ERROR_MESSAGE);
    }

    private void showCard(String cardName) {
        cardLayout.show(cards, cardName);
    }

    private void showMessage(String message, int messageType) {
        JOptionPane.showMessageDialog(frame, message, "Library Management System", messageType);
    }

    public void show() {
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(() -> new LibraryManagementSystem().show());
    }
}
