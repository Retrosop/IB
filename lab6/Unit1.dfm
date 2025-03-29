object Form1: TForm1
  Left = 313
  Top = 129
  Width = 170
  Height = 224
  Caption = 'Form1'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 48
    Top = 16
    Width = 46
    Height = 13
    Caption = 'Password'
  end
  object EditPassword: TEdit
    Left = 16
    Top = 32
    Width = 121
    Height = 21
    PasswordChar = '*'
    TabOrder = 0
  end
  object ButtonEncrypt: TButton
    Left = 16
    Top = 64
    Width = 75
    Height = 25
    Caption = 'ButtonEncrypt'
    TabOrder = 1
  end
  object ButtonDecrypt: TButton
    Left = 56
    Top = 96
    Width = 75
    Height = 25
    Caption = 'ButtonDecrypt'
    TabOrder = 2
  end
  object Memo1: TMemo
    Left = 16
    Top = 136
    Width = 121
    Height = 41
    Lines.Strings = (
      'Memo1')
    ScrollBars = ssVertical
    TabOrder = 3
  end
  object OpenDialog1: TOpenDialog
    Left = 104
    Top = 64
  end
  object SaveDialog1: TSaveDialog
    Left = 16
    Top = 96
  end
end
