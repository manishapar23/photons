import ROOT
RDF = ROOT.ROOT.RDataFrame
ROOT.ROOT.EnableImplicitMT()
import sys,os


Chain = ROOT.TChain("Events")
for path, subdirs, files in os.walk("/cms/xaastorage/NanoAOD/2017/APR20/XtoAAto4G_Signal_official/X1000A100/"):
        for name in files:
                File = os.path.join(path, name)
                if (File.endswith(".root")):
                        print os.path.join(path, name)
                        Chain.Add(File)
Rdf = RDF(Chain)
ROOT.gInterpreter.Declare('#include "rdf_vars2.h"')
Rdf = Rdf.Define("total_weight", "9.59447/107003.")
Rdf = Rdf.Define("AM1", "get_AM(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 30., 2.4, 0, 1)")
Rdf = Rdf.Define("AM2", "get_AM(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 30., 2.4, 2, 3)")
Rdf = Rdf.Define("AM3", "get_AM(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 30., 2.4, 0, 2)")
Rdf = Rdf.Define("AM4", "get_AM(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 30., 2.4, 1, 3)")
Rdf = Rdf.Define("AM5", "get_AM(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 30., 2.4, 0, 3)")
Rdf = Rdf.Define("AM6", "get_AM(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, 30., 2.4, 1, 2)")

Rdf = Rdf.Filter("nPhoton > 3")


H_AM_1_Lazy = Rdf.Histo1D(("H_AM_1", ";Photons 1 and 2 (GeV);events", 100, 0., 200), "AM1", "total_weight")
H_AM_2_Lazy = Rdf.Histo1D(("H_AM_2", ";Photons 3 and 4 (GeV);events", 100, 0., 200), "AM2", "total_weight")
H_AM_3_Lazy = Rdf.Histo1D(("H_AM_3", ";Photons 1 and 3 (GeV);events", 100, 0., 200), "AM3", "total_weight")
H_AM_4_Lazy = Rdf.Histo1D(("H_AM_4", ";Photons 2 and 4 (GeV);events", 100, 0., 200), "AM4", "total_weight")
H_AM_5_Lazy = Rdf.Histo1D(("H_AM_5", ";Photons 1 and 4 (GeV);events", 100, 0., 200), "AM5", "total_weight")
H_AM_6_Lazy = Rdf.Histo1D(("H_AM_6", ";Photons 2 and 3 (GeV);events", 100, 0., 200), "AM6", "total_weight")

H_AM_1 = H_AM_1_Lazy.GetValue()
H_AM_2 = H_AM_2_Lazy.GetValue()
H_AM_3 = H_AM_3_Lazy.GetValue()
H_AM_4 = H_AM_4_Lazy.GetValue()
H_AM_5 = H_AM_5_Lazy.GetValue()
H_AM_6 = H_AM_6_Lazy.GetValue()


C = ROOT.TCanvas()
C.cd()
H_AM_1.Draw("hist")
C.SaveAs("AM1.root")

C1 = ROOT.TCanvas()
C1.cd()
H_AM_2.Draw("hist")
C1.SaveAs("AM2.root")

C2 = ROOT.TCanvas()
C2.cd()
H_AM_3.Draw("hist")
C2.SaveAs("AM3.root")

C3 = ROOT.TCanvas()
C3.cd()
H_AM_4.Draw("hist")
C3.SaveAs("AM4.root")

C4 = ROOT.TCanvas()
C4.cd()
H_AM_5.Draw("hist")
C4.SaveAs("AM5.root")

C5 = ROOT.TCanvas()
C5.cd()
H_AM_6.Draw("hist")
C5.SaveAs("AM6.root")


