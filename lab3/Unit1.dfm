object Form1: TForm1
  Left = 192
  Top = 125
  Width = 348
  Height = 135
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
  object ButtonEncrypt: TButton
    Left = 16
    Top = 16
    Width = 75
    Height = 25
    Caption = 'ButtonEncrypt'
    TabOrder = 0
    OnClick = ButtonEncryptClick
  end
  object ButtonDecrypt: TButton
    Left = 16
    Top = 48
    Width = 75
    Height = 25
    Caption = 'ButtonDecrypt'
    TabOrder = 1
    OnClick = ButtonDecryptClick
  end
  object Memo1: TMemo
    Left = 128
    Top = 0
    Width = 185
    Height = 89
    Lines.Strings = (
      'Memo1')
    TabOrder = 2
  end
  object OpenDialog1: TOpenDialog
    Left = 96
    Top = 16
  end
  object SaveDialog1: TSaveDialog
    Left = 96
    Top = 48
  end
end
