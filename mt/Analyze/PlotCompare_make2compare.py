import os
import ROOT
from ROOT import *

def MakeCompare(rootfile1,histo1,rootfile2,histo2,name,XAxis):

    ROOT.gStyle.SetFrameLineWidth(3)
    ROOT.gStyle.SetLineWidth(3)
    ROOT.gStyle.SetOptStat(0)
    
    
    file1=TFile(rootfile1,"open")
    Histo1=file1.Get(histo1)
#    Histo1.Scale(2.1/35.9)
#    Histo1.Scale(24.57/35.9)
#    Histo1.Scale(33.40/35.9)
#    Histo1.Scale(2.9/35.9)
    Histo1.Scale(33330/35870.0)
    Histo1.Rebin(1)
    print rootfile1,histo1, Histo1.Integral()


    file2=TFile(rootfile2,"open")
    Histo2=file2.Get(histo2)
    Histo2.Rebin(1)
    print rootfile2,histo2, Histo2.Integral()


    Histo1.SetLineColor(2)
    Histo1.SetLineWidth(3)
#    Histo2=file.Get(Cat+'/'+hist2)
    Histo2.SetLineColor(3)
    Histo2.SetLineWidth(3)
#    Histo3=file.Get(Cat+'/'+hist3)
#    Histo3.SetLineColor(4)
#    Histo3.SetLineWidth(2)
#
    Can=TCanvas("canvas","",0,0,600,600)
#
    Histo1.SetTitle('')
    Histo1.GetXaxis().SetTitle(XAxis)
    Histo1.GetXaxis().SetLabelSize(0.04)
    Histo1.GetXaxis().SetNdivisions(505)
    Histo1.GetXaxis().SetTitleSize(0.05)
    Histo1.GetXaxis().SetTitleOffset(0.9)
    Histo1.GetXaxis().SetLabelSize(0.04)
    Histo1.GetXaxis().SetTitleFont(42)
    Histo1.SetMaximum(Histo1.GetMaximum()*2)
#    Histo1.GetXaxis().SetRangeUser(0,1000)
#
#
#
#    
#    
    Histo1.Draw()
    Histo2.Draw('same')
#    Histo3.Draw('same')
#
    leg=TLegend(.3,.7,.9,.9, "", "brNDC")
    leg.SetLineWidth(1)
    leg.SetLineStyle(0)
    leg.SetFillStyle(0)
#    leg.SetBorderSize(0)
    leg.SetTextFont(62)
    leg.AddEntry(Histo1,'ZTT','l')
    leg.AddEntry(Histo2,'Embedded','l')
#    leg.AddEntry(Histo3,hist3.replace("_CMS_scale",""),'l')
    leg.Draw()

    
    
    categ  = ROOT.TPaveText(0.75, 0.5+0.013, 0.97, 0.70+0.155, "NDC")
    categ.SetBorderSize(   0 )
    categ.SetFillStyle(    0 )
    categ.SetTextAlign(   12 )
    categ.SetTextSize ( 0.04 )
    categ.SetTextColor(    1 )
    categ.SetTextFont (   41 )
    categ.AddText(name)
    categ.Draw()
    
    Can.SaveAs('_compare_WSamples_%s.pdf'%histo1)




#rootfile=['data_obs','TT','W','SingleTop','VV','ZTT','Codex_1200','QCD']
#histo='NewROOTdePhiOnlyJet/TotalRootForLimit_PreSelection_MuJet_LQMass_HighMT_HighDPhi_AntiIso.root'

rootfile1='OUTPUTFiles/ZTT_Tot.root'
#rootfile1='files_out_embed/_ZTT_Tot.root'
#rootfile2='emb.root'
#rootfile2='TotalNewEmbedMu.root'
#rootfile2='final_33_5fb.root'
#rootfile2='final_MT_F.root'
rootfile2='OUTPUTFiles/Tot_Embed.root'


histo1='Lep_pt_0jet'
MakeCompare(rootfile1,histo1,rootfile2,histo1,'0jet cat 2/fb','Lep pt  (GeV)')

histo1='Lep_eta_0jet'
MakeCompare(rootfile1,histo1,rootfile2,histo1,'0jet cat 2/fb','Lep eta ')

histo1='Tau_pt_0jet'
MakeCompare(rootfile1,histo1,rootfile2,histo1,'0jet cat 2/fb','Tau pt  (GeV)')

histo1='Tau_eta_0jet'
MakeCompare(rootfile1,histo1,rootfile2,histo1,'0jet cat 2/fb','Tau eta ')


histo1='Higgs_visMass_0jet'
MakeCompare(rootfile1,histo1,rootfile2,histo1,'0jet cat 2/fb','Vis mass  (GeV)')

histo1='Higgs_pt_0jet'
MakeCompare(rootfile1,histo1,rootfile2,histo1,'0jet cat 2/fb','Higgs pT (GeV) ')



#
#histo1='MuJet_LQMass_MT400_HighDPhi_Iso'
#histo2='MuJet_LQMass_MT400_HighDPhi_Iso'
#MakeCompare(rootfile1,histo1,rootfile2,histo2,'MT > 400 GeV')







