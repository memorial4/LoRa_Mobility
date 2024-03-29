//
// Generated file, do not edit! Created by opp_msgtool 6.0 from LoRa/LoRaMacFrame.msg.
//

#ifndef __FLORA_LORAMACFRAME_M_H
#define __FLORA_LORAMACFRAME_M_H

#if defined(__clang__)
#  pragma clang diagnostic ignored "-Wreserved-id-macro"
#endif
#include <omnetpp.h>

// opp_msgtool version check
#define MSGC_VERSION 0x0600
#if (MSGC_VERSION!=OMNETPP_VERSION)
#    error Version mismatch! Probably this file was generated by an earlier version of opp_msgtool: 'make clean' should help.
#endif


namespace flora {

class LoRaMacFrame;

}  // namespace flora

#include "inet/common/INETDefs_m.h" // import inet.common.INETDefs

#include "inet/common/Units_m.h" // import inet.common.Units

#include "inet/linklayer/common/MacAddress_m.h" // import inet.linklayer.common.MacAddress

#include "inet/common/packet/chunk/Chunk_m.h" // import inet.common.packet.chunk.Chunk

// cplusplus {{
using namespace inet;
// }}


namespace flora {

/**
 * Class generated from <tt>LoRa/LoRaMacFrame.msg:31</tt> by opp_msgtool.
 * <pre>
 * class LoRaMacFrame extends inet::FieldsChunk
 * {
 *     inet::MacAddress transmitterAddress;
 *     inet::MacAddress receiverAddress;
 * 
 *     int sequenceNumber;
 *     double LoRaTP;
 *     inet::Hz LoRaCF;
 *     int LoRaSF;
 *     inet::Hz LoRaBW;
 *     int LoRaCR;
 *     bool LoRaUseHeader;
 *     double RSSI;
 *     double SNIR;
 * }
 * </pre>
 */
class LoRaMacFrame : public ::inet::FieldsChunk
{
  protected:
    ::inet::MacAddress transmitterAddress;
    ::inet::MacAddress receiverAddress;
    int sequenceNumber = 0;
    double LoRaTP = 0;
    ::inet::Hz LoRaCF = Hz(NaN);
    int LoRaSF = 0;
    ::inet::Hz LoRaBW = Hz(NaN);
    int LoRaCR = 0;
    bool LoRaUseHeader = false;
    double RSSI = 0;
    double SNIR = 0;

  private:
    void copy(const LoRaMacFrame& other);

  protected:
    bool operator==(const LoRaMacFrame&) = delete;

  public:
    LoRaMacFrame();
    LoRaMacFrame(const LoRaMacFrame& other);
    virtual ~LoRaMacFrame();
    LoRaMacFrame& operator=(const LoRaMacFrame& other);
    virtual LoRaMacFrame *dup() const override {return new LoRaMacFrame(*this);}
    virtual void parsimPack(omnetpp::cCommBuffer *b) const override;
    virtual void parsimUnpack(omnetpp::cCommBuffer *b) override;

    virtual const ::inet::MacAddress& getTransmitterAddress() const;
    virtual ::inet::MacAddress& getTransmitterAddressForUpdate() { handleChange();return const_cast<::inet::MacAddress&>(const_cast<LoRaMacFrame*>(this)->getTransmitterAddress());}
    virtual void setTransmitterAddress(const ::inet::MacAddress& transmitterAddress);

    virtual const ::inet::MacAddress& getReceiverAddress() const;
    virtual ::inet::MacAddress& getReceiverAddressForUpdate() { handleChange();return const_cast<::inet::MacAddress&>(const_cast<LoRaMacFrame*>(this)->getReceiverAddress());}
    virtual void setReceiverAddress(const ::inet::MacAddress& receiverAddress);

    virtual int getSequenceNumber() const;
    virtual void setSequenceNumber(int sequenceNumber);

    virtual double getLoRaTP() const;
    virtual void setLoRaTP(double LoRaTP);

    virtual ::inet::Hz getLoRaCF() const;
    virtual void setLoRaCF(::inet::Hz LoRaCF);

    virtual int getLoRaSF() const;
    virtual void setLoRaSF(int LoRaSF);

    virtual ::inet::Hz getLoRaBW() const;
    virtual void setLoRaBW(::inet::Hz LoRaBW);

    virtual int getLoRaCR() const;
    virtual void setLoRaCR(int LoRaCR);

    virtual bool getLoRaUseHeader() const;
    virtual void setLoRaUseHeader(bool LoRaUseHeader);

    virtual double getRSSI() const;
    virtual void setRSSI(double RSSI);

    virtual double getSNIR() const;
    virtual void setSNIR(double SNIR);
};

inline void doParsimPacking(omnetpp::cCommBuffer *b, const LoRaMacFrame& obj) {obj.parsimPack(b);}
inline void doParsimUnpacking(omnetpp::cCommBuffer *b, LoRaMacFrame& obj) {obj.parsimUnpack(b);}


}  // namespace flora


namespace omnetpp {

template<> inline flora::LoRaMacFrame *fromAnyPtr(any_ptr ptr) { return check_and_cast<flora::LoRaMacFrame*>(ptr.get<cObject>()); }

}  // namespace omnetpp

#endif // ifndef __FLORA_LORAMACFRAME_M_H

