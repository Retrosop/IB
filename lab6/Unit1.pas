unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls;

type
  TForm1 = class(TForm)
    EditPassword: TEdit;
    ButtonEncrypt: TButton;
    ButtonDecrypt: TButton;
    OpenDialog1: TOpenDialog;
    SaveDialog1: TSaveDialog;
    Memo1: TMemo;
    Label1: TLabel;
    procedure ButtonEncryptClick(Sender: TObject);
    procedure ButtonDecryptClick(Sender: TObject);
  private
    { Private declarations }
    procedure AddPasswordToFile(const Password, FileName: string);
    function CheckPassword(const Password, FileName: string): Boolean;
    procedure XORCipher(const InputFile, OutputFile, Password: string);
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

// ?????????? ?????? ? ?????? ?????
procedure TForm1.AddPasswordToFile(const Password, FileName: string);
var
  F: file of Byte;
  TempFile: string;
  i: Integer;
  B: Byte;
begin
  TempFile := ChangeFileExt(FileName, '.tmp');
  AssignFile(F, FileName);
  Rename(F, TempFile); // ??????????????? ???????? ???? ?? ?????????

  AssignFile(F, FileName);
  Rewrite(F);

  // ?????????? ?????? ? ?????? ?????
  for i := 1 to Length(Password) do
  begin
    B := Ord(Password[i]);
    Write(F, B);
  end;

  // ???????? ?????????? ?????????? ?????
  AssignFile(F, TempFile);
  Reset(F);
  while not Eof(F) do
  begin
    Read(F, B);
    Write(F, B);
  end;

  CloseFile(F);
  DeleteFile(TempFile); // ??????? ????????? ????
end;

// ???????? ?????? ? ?????? ?????
function TForm1.CheckPassword(const Password, FileName: string): Boolean;
var
  F: file of Byte;
  i: Integer;
  B: Byte;
  StoredPassword: string;
begin
  Result := False;
  AssignFile(F, FileName);
  Reset(F);

  // ?????? ?????? ?? ?????? ?????
  StoredPassword := '';
  for i := 1 to Length(Password) do
  begin
    if Eof(F) then Break;
    Read(F, B);
    StoredPassword := StoredPassword + Chr(B);
  end;

  CloseFile(F);
  Result := (StoredPassword = Password);
end;

// ??????????/???????????? XOR
procedure TForm1.XORCipher(const InputFile, OutputFile, Password: string);
var
  Fin, Fout: file of Byte;
  P, K: Byte;
  KeyIndex: Integer;
begin
  AssignFile(Fin, InputFile);
  AssignFile(Fout, OutputFile);
  Reset(Fin);
  Rewrite(Fout);

  KeyIndex := 1;
  while not Eof(Fin) do
  begin
    Read(Fin, P);
    K := Ord(Password[KeyIndex]);
    P := P xor K; // XOR-??????????
    Write(Fout, P);

    KeyIndex := (KeyIndex mod Length(Password)) + 1;
  end;

  CloseFile(Fin);
  CloseFile(Fout);
end;

// ?????????? ?????? "???????????"
procedure TForm1.ButtonEncryptClick(Sender: TObject);
var
  Password: string;
begin
  if EditPassword.Text = '' then
  begin
    ShowMessage('??????? ??????!');
    Exit;
  end;

  if OpenDialog1.Execute then
  begin
    if SaveDialog1.Execute then
    begin
      Password := EditPassword.Text;
      XORCipher(OpenDialog1.FileName, SaveDialog1.FileName, Password);
      AddPasswordToFile(Password, SaveDialog1.FileName);
      Memo1.Lines.Add('???? ??????????: ' + SaveDialog1.FileName);
    end;
  end;
end;

// ?????????? ?????? "????????????"
procedure TForm1.ButtonDecryptClick(Sender: TObject);
var
  Password: string;
begin
  Password := EditPassword.Text;
  if Password = '' then
  begin
    ShowMessage('??????? ??????!');
    Exit;
  end;

  if OpenDialog1.Execute then
  begin
    if SaveDialog1.Execute then
    begin
      if not CheckPassword(Password, OpenDialog1.FileName) then
      begin
        ShowMessage('???????? ??????!');
        Exit;
      end;

      XORCipher(OpenDialog1.FileName, SaveDialog1.FileName, Password);
      Memo1.Lines.Add('???? ???????????: ' + SaveDialog1.FileName);
    end;
  end;
end;

end.
