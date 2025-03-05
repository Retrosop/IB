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
  Unit2; // Подключаем модуль с функциями шифрования

procedure TForm1.Button1Click(Sender: TObject);
var
  OriginalText, EncryptedText, DecryptedText: string;
begin
  OriginalText := 'Hello, World! По русски.';
  EncryptedText := EncryptText(OriginalText);
  DecryptedText := DecryptText(EncryptedText);

  ShowMessage('Original: ' + OriginalText + #13#10 +
              'Encrypted: ' + EncryptedText + #13#10 +
              'Decrypted: ' + DecryptedText);
end;

end.
