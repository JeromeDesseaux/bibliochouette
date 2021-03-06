import 'package:barcode_scan/barcode_scan.dart';
import 'package:firebase_auth/firebase_auth.dart';
import "package:flutter/material.dart";
import 'package:firebase_database/firebase_database.dart';
import '../models/loan.dart';
import '../models/book.dart';
import './loan_user.dart';
import 'package:flutter/services.dart';

class LoanBookPage extends StatefulWidget {
  final FirebaseUser user;

  LoanBookPage({Key key, @required this.user}) : super(key: key);

  @override
  State<StatefulWidget> createState() {
    return new _LoanBookPageState(this.user);
  }
}


class _LoanBookPageState extends State<LoanBookPage> {

//class LoanBookPage extends StatelessWidget {

  FirebaseUser user;
  String barcode = "";

  // In the constructor, require a Todo
  _LoanBookPageState(FirebaseUser fuser){
    this.user = fuser;
  }

  Future _scan() async {
    try {
      String barcode = await BarcodeScanner.scan();
      //this._searchBookByISBN(barcode);
      setState(() => this.barcode = barcode);
    } on PlatformException catch (e) {
      if (e.code == BarcodeScanner.CameraAccessDenied) {
        setState(() {
          this.barcode = 'The user did not grant the camera permission!';
        });
      } else {
        setState(() => this.barcode = 'Unknown error: $e');
      }
    } on FormatException{
      setState(() => this.barcode = 'null (User returned using the "back"-button before scanning anything. Result)');
    } catch (e) {
      setState(() => this.barcode = 'Unknown error: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
        appBar: new AppBar(
          title: new Text("BiblioChouette"),
          actions: <Widget>[
            IconButton(
                icon: Icon(Icons.camera),
                onPressed: () {
                  //print("scan book");
                  this._scan();
                },
              ),
          ],
        ),
        body: _manageDisplay(),
        // drawer: new BibDrawer(user: this._user),
        // floatingActionButton: new FloatingActionButton(
        //   elevation: 0.0,
        //   child: new Icon(Icons.add),
        //   backgroundColor: new Color(0xFFE57373),
        //   //onPressed: (){_addLoan();}
        // ),
      );
  }

  // getAvailableBooks() {
  //   var loans = FirebaseDatabase.instance.reference().child("loans").child(user.uid).orderByChild("returnDateValidated").equalTo(null).onValue;
  //   var books = FirebaseDatabase.instance.reference().child("books").child(user.uid);
  // }

  Widget _manageDisplay() {
    if(user != null){
      return new StreamBuilder<Event>(
          stream: FirebaseDatabase.instance.reference().child("books").child(user.uid).orderByChild("title").onValue,
          builder: (BuildContext context, AsyncSnapshot<Event> snapshot) {
            if (!snapshot.hasData) return const Text('No data provided');
            Map<dynamic, dynamic> map = snapshot.data.snapshot.value;
            List<Book> books = [];
            List<String> titles = [];
            map.forEach((i, v) {
              var book = Book.fromJson(new Map<String, dynamic>.from(v), i);
              books.add(book);
              titles.add(book.title);
              books.sort((a,b) => a.title.compareTo(b.title));
            });
            // int bookCount = books.length;
            return new StreamBuilder<Event>(
              stream: FirebaseDatabase.instance.reference().child("loans").child(user.uid).orderByChild("returnDateValidated").equalTo(null).onValue,
              builder: (BuildContext context, AsyncSnapshot<Event> snapshot) {

                if (!snapshot.hasData) return const Text('No data provided');
                Map<dynamic, dynamic> map = snapshot.data.snapshot.value;
                List<Loan> loans = [];
                List<String> loanTitles = [];
                if(map != null) {
                  map.forEach((i, v) {
                    var loan = Loan.fromJson(new Map<String, dynamic>.from(v), i);
                    loans.add(loan);
                    loanTitles.add(loan.book.uid);
                  });
                }

                books.removeWhere((i) => loanTitles.contains(i.uid));

                if(this.barcode.isNotEmpty && (this.barcode.trim().length==13 || this.barcode.trim().length==10)){
                  books = books.where((book) => book.isbn!=null?book.isbn.contains(this.barcode):false).toList();
                }

                return new ListView.builder(
                  itemCount: books.length,
                  itemBuilder: (_, int index) {
                    Book book = books[index];
                    return new ListTile(
                      leading: new CircleAvatar(
                        backgroundImage: new NetworkImage(book.cover),
                      ),
                      title: new Text(book.title?? '<No title>'),
                      subtitle: new Text(book.authors),
                      onTap: () {
                        // print("go to loan page");
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => new LoanUserPage(user: this.user, book: book),
                          ),
                        );
                      },
                      // trailing: new IconButton(
                      //   icon: new Icon(Icons.input),
                      //   onPressed: () {
                      //     this._showDeleteDialog(loan);
                      //   },
                      // )
                    );
                  },
                );
              },

            );
            
            
            
            
          },
        );
    }else{
      return new Text("FETCHING DATA");
    }
  }


}