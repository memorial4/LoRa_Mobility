//
// Generated file, do not edit! Created by opp_msgtool 6.0 from LoRaPhy/LoRaPhyPreamble.msg.
//

#ifndef __FLORA_LORAPHYPREAMBLE_M_H
#define __FLORA_LORAPHYPREAMBLE_M_H

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

class LoRaPhyPreamble;

}  // namespace flora

#include "inet/common/INETDefs_m.h" // import inet.common.INETDefs

#include "inet/common/packet/chunk/Chunk_m.h" // import inet.common.packet.chunk.Chunk

#include "inet/common/Units_m.h" // import inet.common.Units

#include "inet/linklayer/common/MacAddress_m.h" // import inet.linklayer.common.MacAddress

// cplusplus {{
using namespace inet;
// }}


namespace flora {

/**
 * Class generated from <tt>LoRaPhy/LoRaPhyPreamble.msg:27</tt> by opp_msgtool.
 * <pre>
 * class LoRaPhyPreamble extends inet::FieldsChunk
 * {
 *     inet::Hz centerFrequency;
 *     inet::Hz bandwidth;
 *     int spreadFactor;
 *     inet::W power;
 *     bool UseHeader;
 *     int codeRendundance;
 *     inet::MacAddress receiverAddress;
 * }
 * </pre>
 */
class LoRaPhyPreamble : public ::inet::FieldsChunk
{
  protected:
    ::inet::Hz centerFrequency = Hz(NaN);
    ::inet::Hz bandwidth = Hz(NaN);
    int spreadFactor = 0;
    ::inet::W power = W(NaN);
    bool UseHeader = false;
    int codeRendundance = 0;
    ::inet::MacAddress receiverAddress;

  private:
    void copy(const LoRaPhyPreamble& other);

  protected:
    bool operator==(const LoRaPhyPreamble&) = delete;

  public:
    LoRaPhyPreamble();
    LoRaPhyPreamble(const LoRaPhyPreamble& other);
    virtual ~LoRaPhyPreamble();
    LoRaPhyPreamble& operator=(const LoRaPhyPreamble& other);
    virtual LoRaPhyPreamble *dup() const override {return new LoRaPhyPreamble(*this);}
    virtual void parsimPack(omnetpp::cCommBuffer *b) const override;
    virtual void parsimUnpack(omnetpp::cCommBuffer *b) override;

    virtual ::inet::Hz getCenterFrequency() const;
    virtual void setCenterFrequency(::inet::Hz centerFrequency);

    virtual ::inet::Hz getBandwidth() const;
    virtual void setBandwidth(::inet::Hz bandwidth);

    virtual int getSpreadFactor() const;
    virtual void setSpreadFactor(int spreadFactor);

    virtual ::inet::W getPower() const;
    virtual void setPower(::inet::W power);

    virtual bool getUseHeader() const;
    virtual void setUseHeader(bool UseHeader);

    virtual int getCodeRendundance() const;
    virtual void setCodeRendundance(int codeRendundance);

    virtual const ::inet::MacAddress& getReceiverAddress() const;
    virtual ::inet::MacAddress& getReceiverAddressForUpdate() { handleChange();return const_cast<::inet::MacAddress&>(const_cast<LoRaPhyPreamble*>(this)->getReceiverAddress());}
    virtual void setReceiverAddress(const ::inet::MacAddress& receiverAddress);
};

inline void doParsimPacking(omnetpp::cCommBuffer *b, const LoRaPhyPreamble& obj) {obj.parsimPack(b);}
inline void doParsimUnpacking(omnetpp::cCommBuffer *b, LoRaPhyPreamble& obj) {obj.parsimUnpack(b);}


}  // namespace flora


namespace omnetpp {

template<> inline flora::LoRaPhyPreamble *fromAnyPtr(any_ptr ptr) { return check_and_cast<flora::LoRaPhyPreamble*>(ptr.get<cObject>()); }

}  // namespace omnetpp

#endif // ifndef __FLORA_LORAPHYPREAMBLE_M_H

