unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;

type
  TForm1 = class(TForm)
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

uses
  DoubleSquareCipher;

procedure TForm1.Button1Click(Sender: TObject);
var
  Cipher: TDoubleSquareCipher;
  PlainText, EncryptedText, DecryptedText: string;
begin
  Cipher := TDoubleSquareCipher.Create('KEYWORDONE', 'KEYWORDTWO');
  try
    PlainText := 'MIRPRIVET';
    EncryptedText := Cipher.Encrypt(PlainText);
    //DecryptedText := Cipher.Decrypt(EncryptedText);

    ShowMessage('Original: ' + PlainText + #13#10 +
                'Encrypted: ' + EncryptedText + #13#10); // +
                //'Decrypted: ' + DecryptedText);
  finally
    Cipher.Free;
  end;
end;
end.


