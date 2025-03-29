unit DoubleSquareCipher;

interface

uses
  SysUtils, StrUtils;

type
  // Определяем тип для квадрата 5x5
  TSquare = array[0..4, 0..4] of Char;

  TDoubleSquareCipher = class
  private
    FSquare1, FSquare2: TSquare; // Два квадрата 5x5
    procedure InitializeSquares(const Key1, Key2: string);
    function FindCharPosition(const Square: TSquare; C: Char; out Row, Col: Integer): Boolean;
  public
    constructor Create(const Key1, Key2: string);
    function Encrypt(const PlainText: string): string;
    function Decrypt(const CipherText: string): string;
  end;

implementation

constructor TDoubleSquareCipher.Create(const Key1, Key2: string);
begin
  InitializeSquares(Key1, Key2);
end;

// Инициализация квадратов на основе ключей
procedure TDoubleSquareCipher.InitializeSquares(const Key1, Key2: string);
var
  i, j, k: Integer;
  UsedChars: string;
begin
  UsedChars := '';
  k := 1;

  // Заполнение первого квадрата
  for i := 0 to 4 do
    for j := 0 to 4 do
    begin
      while (k <= Length(Key1)) and (Pos(Key1[k], UsedChars) > 0) do
        Inc(k);
      if k <= Length(Key1) then
      begin
        FSquare1[i, j] := Key1[k];
        UsedChars := UsedChars + Key1[k];
      end
      else
        FSquare1[i, j] := Chr(Ord('A') + i * 5 + j);
      Inc(k);
    end;

  UsedChars := '';
  k := 1;

  // Заполнение второго квадрата
  for i := 0 to 4 do
    for j := 0 to 4 do
    begin
      while (k <= Length(Key2)) and (Pos(Key2[k], UsedChars) > 0) do
        Inc(k);
      if k <= Length(Key2) then
      begin
        FSquare2[i, j] := Key2[k];
        UsedChars := UsedChars + Key2[k];
      end
      else
        FSquare2[i, j] := Chr(Ord('A') + i * 5 + j);
      Inc(k);
    end;
end;

// Поиск позиции символа в квадрате
function TDoubleSquareCipher.FindCharPosition(const Square: TSquare; C: Char; out Row, Col: Integer): Boolean;
var
  i, j: Integer;
begin
  for i := 0 to 4 do
    for j := 0 to 4 do
      if Square[i, j] = C then
      begin
        Row := i;
        Col := j;
        Result := True;
        Exit;
      end;
  Result := False;
end;

// Шифрование текста
function TDoubleSquareCipher.Encrypt(const PlainText: string): string;
var
  i, Row1, Col1, Row2, Col2: Integer;
  C1, C2: Char;
begin
  Result := '';
  for i := 1 to Length(PlainText) div 2 do
  begin
    C1 := PlainText[i * 2 - 1];
    C2 := PlainText[i * 2];

    if FindCharPosition(FSquare1, C1, Row1, Col1) and FindCharPosition(FSquare2, C2, Row2, Col2) then
    begin
      Result := Result + FSquare1[Row1, Col2] + FSquare2[Row2, Col1];
    end;
  end;
end;

// Дешифрование текста
function TDoubleSquareCipher.Decrypt(const CipherText: string): string;
var
  i, Row1, Col1, Row2, Col2: Integer;
  C1, C2: Char;
begin
  Result := '';
  for i := 1 to Length(CipherText) div 2 do
  begin
    C1 := CipherText[i * 2 - 1];
    C2 := CipherText[i * 2];

    if FindCharPosition(FSquare1, C1, Row1, Col2) and FindCharPosition(FSquare2, C2, Row2, Col1) then
    begin
      Result := Result + FSquare1[Row1, Col1] + FSquare2[Row2, Col2];
    end;
  end;
end;

end. 
