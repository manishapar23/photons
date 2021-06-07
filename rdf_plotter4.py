#RDF plotter
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
ROOT.gInterpreter.Declare('#include "rdf_vars3.h"')
Rdf = Rdf.Define("total_weight", "9.59447/107003.")
Rdf = Rdf.Define("passCUT", "get_CUT(nPhoton, Photon_mass, Photon_pt, Photon_eta, Photon_phi, Photon_mvaID_WP90, 30., 2.4)")
# cut passes npho, pt, eta, phi, photon ID
CUT = "passCUT==1."
Rdf = Rdf.Filter(CUT)


H_Phoeta_Lazy = Rdf.Histo1D(("H_Phoeta",";eta;events", 100, 0., 3.), "Photon_eta", "total_weight")
H_Phophi_Lazy = Rdf.Histo1D(("H_Phophi",";phi;events", 100, 0., 4.), "Photon_phi", "total_weight")
H_nphoton_Lazy = Rdf.Histo1D(("H_nphoton",";mass;events", 100, 0., 10.), "nPhoton", "total_weight")
H_Phopt_Lazy = Rdf.Histo1D(("H_Phopt",";pt;events", 100, 0., 1000.), "Photon_pt", "total_weight")

H_Phoeta = H_Phoeta_Lazy.GetValue()
H_Phophi = H_Phophi_Lazy.GetValue()
H_nphoton = H_nphoton_Lazy.GetValue()
H_Phopt = H_Phopt_Lazy.GetValue()

myfile = ROOT.TFile('test2.root', 'RECREATE')
C1 = ROOT.TCanvas()
C1.cd()
H_Phoeta.Draw("hist")
C1.SaveAs("phoeta.root")

C2 = ROOT.TCanvas()
C2.cd()
H_Phophi.Draw("hist")
C2.SaveAs("phophi.root")

C3 = ROOT.TCanvas()
C3.cd()
H_nphoton.Draw("hist")
C3.SaveAs("nphoton.root")

C4 = ROOT.TCanvas()
C4.cd()
H_Phopt.Draw("hist")
C4.SaveAs("phopt.root")
