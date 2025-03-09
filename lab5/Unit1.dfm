object Form1: TForm1
  Left = 192
  Top = 125
  Width = 170
  Height = 219
  Caption = 'Form1'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 40
    Top = 16
    Width = 17
    Height = 17
    Caption = 'P'
  end
  object Label2: TLabel
    Left = 72
    Top = 16
    Width = 17
    Height = 17
    Caption = 'G'
  end
  object Label3: TLabel
    Left = 104
    Top = 16
    Width = 17
    Height = 17
    Caption = 'A'
  end
  object EditP: TEdit
    Left = 32
    Top = 32
    Width = 25
    Height = 21
    TabOrder = 0
  end
  object EditG: TEdit
    Left = 64
    Top = 32
    Width = 25
    Height = 21
    TabOrder = 1
  end
  object EditA: TEdit
    Left = 96
    Top = 32
    Width = 25
    Height = 21
    TabOrder = 2
  end
  object ButtonEncrypt: TButton
    Left = 24
    Top = 64
    Width = 75
    Height = 25
    Caption = 'ButtonEncrypt'
    TabOrder = 3
  end
  object Button1: TButton
    Left = 56
    Top = 128
    Width = 17
    Height = 1
    Caption = 'Button1'
    TabOrder = 4
  end
  object ButtonDecrypt: TButton
    Left = 24
    Top = 96
    Width = 75
    Height = 25
    Caption = 'ButtonDecrypt'
    TabOrder = 5
  end
  object Memo1: TMemo
    Left = 16
    Top = 128
    Width = 121
    Height = 41
    Lines.Strings = (
      'Memo1')
    TabOrder = 6
  end
  object OpenDialog1: TOpenDialog
    Left = 104
    Top = 64
  end
  object SaveDialog1: TSaveDialog
    Left = 104
    Top = 96
  end
end
