unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;

type
  TForm1 = class(TForm)
    EditP: TEdit;
    EditG: TEdit;
    EditA: TEdit;
    ButtonEncrypt: TButton;
    ButtonDecrypt: TButton;
    OpenDialog1: TOpenDialog;
    SaveDialog1: TSaveDialog;
    Memo1: TMemo;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    procedure ButtonEncryptClick(Sender: TObject);
    procedure ButtonDecryptClick(Sender: TObject);
    procedure FormCreate(Sender: TObject); // Добавлен метод FormCreate
  private
    { Private declarations }
    function PowerMod(base, exponent, modulus: Integer): Integer;
    procedure ElGamalCipher(const InputFile, OutputFile: string; EncryptMode: Boolean);
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

// Функция для вычисления (base^exponent) mod modulus
function TForm1.PowerMod(base, exponent, modulus: Integer): Integer;

begin
  result := 1;
  base := base mod modulus;
  while exponent > 0 do
  begin
    if (exponent and 1) = 1 then
      result := (result * base) mod modulus;
    base := (base * base) mod modulus;
    exponent := exponent shr 1;
  end;
  Result := result;
end;

// Процедура шифрования/дешифрования
procedure TForm1.ElGamalCipher(const InputFile, OutputFile: string; EncryptMode: Boolean);
var
  Fin, Fout: file of Integer;
  P, Y, Y1, Y2, K: Integer;
  p_val, g_val, a_val: Integer;
begin
  // Получение параметров из полей ввода
  p_val := StrToInt(EditP.Text);
  g_val := StrToInt(EditG.Text);
  a_val := StrToInt(EditA.Text);

  // Вычисление открытого ключа Y = g^a mod p
  Y := PowerMod(g_val, a_val, p_val);

  AssignFile(Fin, InputFile);
  AssignFile(Fout, OutputFile);
  Reset(Fin);
  Rewrite(Fout);

  // Для шифрования используем случайный K (здесь K=3 для примера)
  K := 3; // В реальном коде K должно быть случайным и взаимно простым с p-1

  if EncryptMode then
  begin
    // Шифрование: запись Y1 и Y2 в файл
    while not Eof(Fin) do
    begin
      Read(Fin, P);
      Y1 := PowerMod(g_val, K, p_val);
      Y2 := (PowerMod(Y, K, p_val) xor P); // Шифрование: Y2 = (Y^K mod p) xor P
      Write(Fout, Y1);
      Write(Fout, Y2);
    end;
    Memo1.Lines.Add('Файл зашифрован: ' + OutputFile);
  end
  else
  begin
    // Дешифрование: чтение Y1 и Y2 из файла
    while not Eof(Fin) do
    begin
      Read(Fin, Y1);
      Read(Fin, Y2);
      P := (PowerMod(Y1, a_val, p_val) xor Y2); // Дешифрование: P = (Y1^a mod p) xor Y2
      Write(Fout, P);
    end;
    Memo1.Lines.Add('Файл расшифрован: ' + OutputFile);
  end;

  CloseFile(Fin);
  CloseFile(Fout);
end;

// Обработчик кнопки "Зашифровать"
procedure TForm1.ButtonEncryptClick(Sender: TObject);
begin
  if OpenDialog1.Execute then
  begin
    if SaveDialog1.Execute then
    begin
      ElGamalCipher(OpenDialog1.FileName, SaveDialog1.FileName, True);
    end;
  end;
end;

// Обработчик кнопки "Расшифровать"
procedure TForm1.ButtonDecryptClick(Sender: TObject);
begin
  if OpenDialog1.Execute then
  begin
    if SaveDialog1.Execute then
    begin
      ElGamalCipher(OpenDialog1.FileName, SaveDialog1.FileName, False);
    end;
  end;
end;

// Метод FormCreate
procedure TForm1.FormCreate(Sender: TObject);
begin
  Memo1.Lines.Add('Форма создана');
end;

end.
