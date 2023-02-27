
from fancytexts import font
#TextStyleList = ['SmallCapsFontDict','CurrencyFontDict','AntrophobiaFont','DoubleStruckFont','BubbleFont','FrakturFont','BoldFrakturFont','FlakyFontDict','MangaFontDict','BlockFontDict','RusifyFontDict','BlackBubbleFontDict','BoldScriptFontDict','HandWritingFontDict','SmoothFontDict','BoldFontDict','ItalicFontDict','BoldItalicFont','MonospaceFontDict','SorcererFontDict','HighAboveFontDict','SpacingFontDict','SquareFontDict','BlurryFontDict','TinyCapsFontDict','BlacksquareFontDict','Fancystyle1Font','Fancystyle2Font','Fancystyle3Font','SymbolsFontDict']


def fancytext(style, text):
    try:
        if style == 'scf':
            def SmallCapsFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.SmallCapsFontDict:
                        spaces += font.SmallCapsFontDict[i]
                    else:
                        spaces += i
                return spaces
            return SmallCapsFontDict(text)


        if style == 'cf':
            def CurrencyFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.CurrencyFontDict:
                        spaces += font.CurrencyFontDict[i]
                    else:
                        spaces += i
                return spaces
            return CurrencyFontDict(text)       


        if style == 'af':
            def AntrophobiaFont(text):
                spaces = ''
                for i in text:
                    if i in font.AntrophobiaFont:
                        spaces += font.AntrophobiaFont[i]
                    else:
                        spaces += i
                return spaces
            return AntrophobiaFont(text)       

        if style == 'dsf':
            def DoubleStruckFont(text):
                spaces = ''
                for i in text:
                    if i in font.DoubleStruckFont:
                        spaces += font.DoubleStruckFont[i]
                    else:
                        spaces += i
                return spaces
            return DoubleStruckFont(text)       


        if style == 'bf':
            def BubbleFont(text):
                spaces = ''
                for i in text:
                    if i in font.BubbleFont:
                        spaces += font.BubbleFont[i]
                    else:
                        spaces += i
                return spaces
            return BubbleFont(text)       


        if style == 'ff':
            def FrakturFont(text):
                spaces = ''
                for i in text:
                    if i in font.FrakturFont:
                        spaces += font.FrakturFont[i]
                    else:
                        spaces += i
                return spaces
            return FrakturFont(text)       
        
        if style == 'bff':
            def BoldFrakturFont(text):
                spaces = ''
                for i in text:
                    if i in font.BoldFrakturFont:
                        spaces += font.BoldFrakturFont[i]
                    else:
                        spaces += i
                return spaces
            return BoldFrakturFont(text)       
        
        if style == 'ffd':
            def FlakyFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.FlakyFontDict:
                        spaces += font.FlakyFontDict[i]
                    else:
                        spaces += i
                return spaces
            return FlakyFontDict(text)       
        
        if style == 'mfd':
            def MangaFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.MangaFontDict:
                        spaces += font.MangaFontDict[i]
                    else:
                        spaces += i
                return spaces
            return MangaFontDict(text)       
        
        if style == 'bfd':
            def BlockFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.BlockFontDict:
                        spaces += font.BlockFontDict[i]
                    else:
                        spaces += i
                return spaces
            return BlockFontDict(text)       
        
        if style == 'rfd':
            def RusifyFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.RusifyFontDict:
                        spaces += font.RusifyFontDict[i]
                    else:
                        spaces += i
                return spaces
            return RusifyFontDict(text)       
        
        if style == 'bbfd':
            def BlackBubbleFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.BlackBubbleFontDict:
                        spaces += font.BlackBubbleFontDict[i]
                    else:
                        spaces += i
                return spaces
            return BlackBubbleFontDict(text)       
        
        if style == 'bsfd':
            def BoldScriptFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.BoldScriptFontDict:
                        spaces += font.BoldScriptFontDict[i]
                    else:
                        spaces += i
                return spaces
            return BoldScriptFontDict(text)       
        
        if style == 'hwfd':
            def HandWritingFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.HandWritingFontDict:
                        spaces += font.HandWritingFontDict[i]
                    else:
                        spaces += i
                return spaces
            return HandWritingFontDict(text)       
        
        if style == 'sfd':
            def SmoothFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.SmoothFontDict:
                        spaces += font.SmoothFontDict[i]
                    else:
                        spaces += i
                return spaces
            return SmoothFontDict(text)       
        
        if style == 'bfds':
            def BoldFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.BoldFontDict:
                        spaces += font.BoldFontDict[i]
                    else:
                        spaces += i
                return spaces
            return BoldFontDict(text)       
        
        if style == 'ifds':
            def ItalicFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.ItalicFontDict:
                        spaces += font.ItalicFontDict[i]
                    else:
                        spaces += i
                return spaces
            return ItalicFontDict(text)       
        
        if style == 'bifd':
            def BoldItalicFont(text):
                spaces = ''
                for i in text:
                    if i in font.BoldItalicFont:
                        spaces += font.BoldItalicFont[i]
                    else:
                        spaces += i
                return spaces
            return BoldItalicFont(text)       
        
        if style == 'mofd':
            def MonospaceFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.MonospaceFontDict:
                        spaces += font.MonospaceFontDict[i]
                    else:
                        spaces += i
                return spaces
            return MonospaceFontDict(text)    
        
        if style == 'sofd':
            def SorcererFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.SorcererFontDict:
                        spaces += font.SorcererFontDict[i]
                    else:
                        spaces += i
                return spaces
            return SorcererFontDict(text)    
        
        if style == 'hiafd':
            def HighAboveFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.HighAboveFontDict:
                        spaces += font.HighAboveFontDict[i]
                    else:
                        spaces += i
                return spaces
            return HighAboveFontDict(text)    
        
        if style == 'spfd':
            def SpacingFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.SpacingFontDict:
                        spaces += font.SpacingFontDict[i]
                    else:
                        spaces += i
                return spaces
            return SpacingFontDict(text)    
        
        if style == 'sqfd':
            def SquareFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.SquareFontDict:
                        spaces += font.SquareFontDict[i]
                    else:
                        spaces += i
                return spaces
            return SquareFontDict(text)    
        
        if style == 'blfd':
            def BlurryFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.BlurryFontDict:
                        spaces += font.BlurryFontDict[i]
                    else:
                        spaces += i
                return spaces
            return BlurryFontDict(text)    
        
        if style == 'ticfd':
            def TinyCapsFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.TinyCapsFontDict:
                        spaces += font.TinyCapsFontDict[i]
                    else:
                        spaces += i
                return spaces
            return TinyCapsFontDict(text)    
        
        if style == 'blsfd':
            def BlacksquareFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.BlacksquareFontDict:
                        spaces += font.BlacksquareFontDict[i]
                    else:
                        spaces += i
                return spaces
            return BlacksquareFontDict(text)    
        
        if style == 'fs1f':
            def Fancystyle1Font(text):
                spaces = ''
                for i in text:
                    if i in font.Fancystyle1Font:
                        spaces += font.Fancystyle1Font[i]
                    else:
                        spaces += i
                return spaces
            return Fancystyle1Font(text)    
        
        if style == 'fs2f':
            def Fancystyle2Font(text):
                spaces = ''
                for i in text:
                    if i in font.Fancystyle2Font:
                        spaces += font.Fancystyle2Font[i]
                    else:
                        spaces += i
                return spaces
            return Fancystyle2Font(text)    
        
        if style == 'fs3f':
            def Fancystyle3Font(text):
                spaces = ''
                for i in text:
                    if i in font.Fancystyle3Font:
                        spaces += font.Fancystyle3Font[i]
                    else:
                        spaces += i
                return spaces
            return Fancystyle3Font(text)   
        
        if style == 'syfd':
            def SymbolsFontDict(text):
                spaces = ''
                for i in text:
                    if i in font.SymbolsFontDict:
                        spaces += font.SymbolsFontDict[i]
                    else:
                        spaces += i
                return spaces
            return SymbolsFontDict(text)   
        
    except:
        return 'Error'




